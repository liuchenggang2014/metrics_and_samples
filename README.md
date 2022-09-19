# metrics_and_samples

## write batch timeseries points data into cloud monitor directly

batch_metrics.py


## pull metrics by binary prometheus exporter

- step 1: install the prometheus binary
```
wget https:////storage.googleapis.com/kochasoft/gsp1026/prometheus
chmod a+x prometheus
```

- step 2: config the prometheus.yml and change the project_id, location, namespace to your config
```
  external_labels:
    project_id: cliu201
    location: us-central1-a
    namespace: local-testing
```

- step 3: long running the prometheus exporter
```
./prometheus --config.file=./prometheus.yml
```

- step 4: generate the metrics and post into the localhost:port//metrics endpoint
```
go mod init packagename
go get github.com/prometheus/client_golang/prometheus
go mod tidy
go run local_metris.go
```

## reference document
- [Collect Metrics from Exporters using the Managed Service for Prometheus](https://www.cloudskillsboost.google/focuses/33339?parent=catalog&qlcampaign=5m-nurturecampaign-62)

- [go client for prometheus hello world](https://www.sentinelone.com/blog/prometheus-metrics-by-example/)

- [gcp official doc](https://cloud.google.com/stackdriver/docs/managed-prometheus/setup-unmanaged#gmp-binary)


