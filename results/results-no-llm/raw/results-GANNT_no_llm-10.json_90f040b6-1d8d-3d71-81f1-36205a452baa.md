## Configuration (2025-06-02_09-08+0200 -- GANNT_no_llm-10.json_90f040b6-1d8d-3d71-81f1-36205a452baa)
```json
{
  "cache_dir" : "./cache/GANNT",
  "gold_standard_configuration" : {
    "hasHeader" : true,
    "path" : "./datasets/req2req/GANNT/answer.csv",
    "swap_columns" : false
  },
  "source_artifact_provider" : {
    "name" : "text",
    "args" : {
      "artifact_type" : "requirement",
      "path" : "./datasets/req2req/GANNT/high"
    }
  },
  "target_artifact_provider" : {
    "name" : "text",
    "args" : {
      "artifact_type" : "requirement",
      "path" : "./datasets/req2req/GANNT/low"
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
      "max_results" : "10"
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
    "name" : "req2req",
    "args" : { }
  }
}
```

## Stats
* #TraceLinks (GS): 68
* #Source Artifacts: 17
* #Target Artifacts: 69
## Results
* True Positives: 46
* False Positives: 124
* False Negatives: 22
* Precision: 0.27058823529411763
* Recall: 0.6764705882352942
* F1: 0.3865546218487395
