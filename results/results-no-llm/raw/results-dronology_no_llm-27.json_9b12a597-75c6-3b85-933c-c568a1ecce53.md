## Configuration (2025-06-02_09-08+0200 -- dronology_no_llm-27.json_9b12a597-75c6-3b85-933c-c568a1ecce53)
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
      "max_results" : "27"
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
* True Positives: 210
* False Positives: 2463
* False Negatives: 10
* Precision: 0.07856341189674523
* Recall: 0.9545454545454546
* F1: 0.14517801590044935
