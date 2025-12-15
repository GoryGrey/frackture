import json

# Load and check the benchmark results
with open('benchmarks/results/benchmark_results_20251215_063946.json') as f:
    data = json.load(f)
    
# Check structure
results = data['results']
dataset = 'small_text'
if dataset in results:
    print(f'Dataset: {dataset}')
    dataset_results = results[dataset]
    print(f'Type: {type(dataset_results)}')
    
    if isinstance(dataset_results, list) and dataset_results:
        print(f'Number of results: {len(dataset_results)}')
        first_result = dataset_results[0]
        print('First result keys:', list(first_result.keys())[:15])
        print('Name:', first_result.get('name'))
        print('Payload size:', first_result.get('serialized_total_bytes'))
        print('Payload is 96B:', first_result.get('payload_is_96b'))
        print('Baseline MSE:', first_result.get('baseline_mse'))
        
        # Get all Frackture results
        frackture_results = [r for r in dataset_results if r.get('name') == 'Frackture']
        if frackture_results:
            print(f'Found {len(frackture_results)} Frackture results')
            for i, r in enumerate(frackture_results):
                print(f'  Result {i+1}:')
                print(f'    Payload size: {r.get("serialized_total_bytes")}')
                print(f'    Baseline MSE: {r.get("baseline_mse")}')
                print(f'    Optimization improvement %: {r.get("optimization_improvement_pct")}')
    else:
        print('No results found or wrong type')