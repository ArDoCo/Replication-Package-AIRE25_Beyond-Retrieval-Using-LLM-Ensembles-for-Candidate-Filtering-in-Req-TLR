## Configuration (2025-06-02_09-08+0200 -- dronology_no_llm-18.json_c3166725-f61c-38be-b59d-f3b0334e6b6d)
```json
{
  "cache_dir" : "./cache/dronology",
  "gold_standard_configuration" : {
    "hasHeader" : true,
    "path" : "./datasets/req2req/dronology/answer.csv",
    "swap_columns" : false
  },
  "source_artifact_provider" : {
    "name" : "text",
    "args" : {
      "artifact_type" : "requirement",
      "path" : "./datasets/req2req/dronology/high"
    }
  },
  "target_artifact_provider" : {
    "name" : "text",
    "args" : {
      "artifact_type" : "requirement",
      "path" : "./datasets/req2req/dronology/low"
    }
  },
  "source_preprocessor" : {
    "name" : "artifact",
    "args" : { }
  },
  "target_preprocessor" : {
    "name" : "artifact",
    "args" : { }
  },
  "embedding_creator" : {
    "name" : "openai",
    "args" : {
      "model" : "text-embedding-3-large"
    }
  },
  "source_store" : {
    "name" : "custom",
    "args" : { }
  },
  "target_store" : {
    "name" : "custom",
    "args" : {
      "max_results" : "18"
    }
  },
  "classifier" : {
    "name" : "mock",
    "args" : { }
  },
  "result_aggregator" : {
    "name" : "any_connection",
    "args" : {
      "source_granularity" : "0",
      "target_granularity" : "0"
    }
  },
  "tracelinkid_postprocessor" : {
    "name" : "identity",
    "args" : { }
  }
}
```

## Stats
* #TraceLinks (GS): 220
* #Source Artifacts: 99
* #Target Artifacts: 211
## Results
* True Positives: 204
* False Positives: 1578
* False Negatives: 16
* Precision: 0.11447811447811448
* Recall: 0.9272727272727272
* F1: 0.20379620379620383
