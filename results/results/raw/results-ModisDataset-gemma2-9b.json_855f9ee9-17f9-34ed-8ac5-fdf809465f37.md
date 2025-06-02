## Configuration (2025-06-02_17-59+0200 -- ModisDataset-gemma2-9b.json_855f9ee9-17f9-34ed-8ac5-fdf809465f37)
```json
{
  "cache_dir" : "./cache-r2r/ModisDataset-ensemble",
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
    "name" : "mock",
    "args" : { }
  },
  "source_store" : {
    "name" : "custom",
    "args" : { }
  },
  "target_store" : {
    "name" : "custom",
    "args" : {
      "max_results" : "infinity"
    }
  },
  "classifiers" : [ [ {
    "name" : "simple_ollama",
    "args" : {
      "model" : "gemma2:9b",
      "seed" : "133742243",
      "template" : "Question: Here are two parts of software development artifacts.\n\n{source_type}: '''{source_content}'''\n\n{target_type}: '''{target_content}'''\nAre they related?\n\nAnswer with 'yes' or 'no'.\n"
    }
  } ] ],
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
* True Positives: 41
* False Positives: 613
* False Negatives: 0
* Precision: 0.06269113149847094
* Recall: 1.0
* F1: 0.11798561151079137
