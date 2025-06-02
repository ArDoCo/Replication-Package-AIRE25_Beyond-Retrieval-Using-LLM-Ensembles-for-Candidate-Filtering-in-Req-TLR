## Configuration (2025-06-02_09-08+0200 -- ModisDataset_no_llm-16.json_c5b54502-b309-3a77-894e-a717136a621b)
```json
{
  "cache_dir" : "./cache/ModisDataset",
  "gold_standard_configuration" : {
    "hasHeader" : true,
    "path" : "./datasets/req2req/ModisDataset/answer.csv",
    "swap_columns" : false
  },
  "source_artifact_provider" : {
    "name" : "text",
    "args" : {
      "artifact_type" : "requirement",
      "path" : "./datasets/req2req/ModisDataset/high"
    }
  },
  "target_artifact_provider" : {
    "name" : "text",
    "args" : {
      "artifact_type" : "requirement",
      "path" : "./datasets/req2req/ModisDataset/low"
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
      "max_results" : "16"
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
* #TraceLinks (GS): 41
* #Source Artifacts: 19
* #Target Artifacts: 49
## Results
* True Positives: 27
* False Positives: 277
* False Negatives: 14
* Precision: 0.08881578947368421
* Recall: 0.6585365853658537
* F1: 0.1565217391304348
