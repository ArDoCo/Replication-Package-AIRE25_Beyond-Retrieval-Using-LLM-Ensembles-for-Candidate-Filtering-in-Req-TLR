## Configuration (2025-06-02_09-08+0200 -- CM1-NASA_no_llm-24.json_688fd7bb-2bcd-326b-8cd8-9682dbd9483a)
```json
{
  "cache_dir" : "./cache/CM1-NASA",
  "gold_standard_configuration" : {
    "hasHeader" : true,
    "path" : "./datasets/req2req/CM1-NASA/answer.csv",
    "swap_columns" : false
  },
  "source_artifact_provider" : {
    "name" : "text",
    "args" : {
      "artifact_type" : "requirement",
      "path" : "./datasets/req2req/CM1-NASA/high"
    }
  },
  "target_artifact_provider" : {
    "name" : "text",
    "args" : {
      "artifact_type" : "requirement",
      "path" : "./datasets/req2req/CM1-NASA/low"
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
      "max_results" : "24"
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
* #TraceLinks (GS): 45
* #Source Artifacts: 22
* #Target Artifacts: 53
## Results
* True Positives: 45
* False Positives: 483
* False Negatives: 0
* Precision: 0.08522727272727272
* Recall: 1.0
* F1: 0.15706806282722513
