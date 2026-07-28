# Availability SLO Example

**Service**: checkout-api  
**SLI**: Successful requests / Total requests (non-5xx)  
**SLO**: 99.9% over 30 days  
**Error Budget**: 0.1% ≈ 43.2 minutes of downtime per month

## Measurement

```promql
sum(rate(http_requests_total{status!~"5.."}[5m]))
/
sum(rate(http_requests_total[5m]))
```
