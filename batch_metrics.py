from google.cloud import monitoring_v3
import time
from google.cloud import bigquery
import pandas

project_id = 'cliu201'
client = monitoring_v3.MetricServiceClient()
project_name = f"projects/{project_id}"

if __name__ == "__main__":
    now = time.time()
    seconds = int(now)
    print(f'seconds:%d', seconds)
    nanos = int((now - seconds) * 10 ** 9)
    interval = monitoring_v3.TimeInterval(
        {"end_time": {"seconds": seconds, "nanos": nanos}}
    )

    interval2 = monitoring_v3.TimeInterval(
        {"end_time": {"seconds": seconds+60, "nanos": nanos}}
    )

    # iterate the requery test and build the timeseries point object by game name
    sql = """
        SELECT gamename, sum(rounds) as sumd FROM `cliu201.ds201.metric_test` 
        group by gamename
    """

    bq_client = bigquery.Client()
    df = bq_client.query(sql).to_dataframe()

    series = []

    for i,j in df.iterrows():
        #print('i: ' + str(i))
        #print('j: ' + str(j))
        #print('j[0]' + str(j[0]))
        series.append(monitoring_v3.TimeSeries())
        series[i].metric.type = "custom.googleapis.com/my_metric_mygames_global"
        series[i].metric.labels["game_name"] = j[0] 

        # https://cloud.google.com/monitoring/api/resources#tag_generic_task
        series[i].resource.type = "global"

        point = monitoring_v3.Point({"interval": interval, "value": {"double_value": j[1]}})
        series[i].points = [point]

        print(series[i].points)
        
#        point2 = monitoring_v3.Point({"interval": interval2, "value": {"double_value": j[1]}})
#        series[i].points.append(point2)
        # print(series[i].points)        
    # for i,j in df.iterrows():
    #     #series.append(monitoring_v3.TimeSeries())
    #     series[i+1].metric.type = "custom.googleapis.com/my_metric_mygames_global"
    #     series[i+1].metric.labels["game_name"] = j[0]

    #     # https://cloud.google.com/monitoring/api/resources#tag_generic_task
    #     series[i+1].resource.type = "global"

    #     point = monitoring_v3.Point({"interval": interval2, "value": {"double_value": j[1]}})
    #     series[i+1].points = [point]

    client.create_time_series(name=project_name, time_series=series)








