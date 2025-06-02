## Configuration (2025-06-02_09-08+0200 -- dronology_no_llm-15.json_04173e79-c03b-3a01-bb7d-2098a58d29f3)
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
      "max_results" : "15"
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
* True Positives: 197
* False Positives: 1288
* False Negatives: 23
* Precision: 0.13265993265993267
* Recall: 0.8954545454545455
* F1: 0.23108504398826982
