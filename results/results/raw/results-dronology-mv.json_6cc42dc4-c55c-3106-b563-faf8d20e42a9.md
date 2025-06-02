## Configuration (2025-06-02_17-59+0200 -- dronology-mv.json_6cc42dc4-c55c-3106-b563-faf8d20e42a9)
```json
{
  "cache_dir" : "./cache-r2r/dronology-ensemble",
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
      "model" : "gemma2:2b",
      "seed" : "133742243",
      "template" : "Question: Here are two parts of software development artifacts.\n\n{source_type}: '''{source_content}'''\n\n{target_type}: '''{target_content}'''\nAre they related?\n\nAnswer with 'yes' or 'no'.\n"
    }
  } ], [ {
    "name" : "simple_ollama",
    "args" : {
      "model" : "gemma2:9b",
      "seed" : "133742243",
      "template" : "Question: Here are two parts of software development artifacts.\n\n{source_type}: '''{source_content}'''\n\n{target_type}: '''{target_content}'''\nAre they related?\n\nAnswer with 'yes' or 'no'.\n"
    }
  }, {
    "name" : "simple_ollama",
    "args" : {
      "model" : "phi4",
      "seed" : "133742243",
      "template" : "Question: Here are two parts of software development artifacts.\n\n{source_type}: '''{source_content}'''\n\n{target_type}: '''{target_content}'''\nAre they related?\n\nAnswer with 'yes' or 'no'.\n"
    }
  }, {
    "name" : "simple_ollama",
    "args" : {
      "model" : "mistral-nemo",
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
* #TraceLinks (GS): 220
* #Source Artifacts: 99
* #Target Artifacts: 211
## Results
* True Positives: 219
* False Positives: 5281
* False Negatives: 1
* Precision: 0.039818181818181815
* Recall: 0.9954545454545455
* F1: 0.07657342657342656
