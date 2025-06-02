## Configuration (2025-06-02_09-08+0200 -- ModisDataset_no_llm-13.json_9de5d0b9-cafd-3c5f-bde6-3e7aa707b281)
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
      "max_results" : "13"
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
* True Positives: 23
* False Positives: 224
* False Negatives: 18
* Precision: 0.0931174089068826
* Recall: 0.5609756097560976
* F1: 0.15972222222222224
