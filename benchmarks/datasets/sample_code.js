// Sample JavaScript module
function fibonacci(n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

class DataProcessor {
    constructor(options) {
        this.options = options || {};
        this.cache = new Map();
    }
    
    process(data) {
        if (this.cache.has(data)) {
            return this.cache.get(data);
        }
        
        const result = data.map(item => item * 2).filter(x => x > 10);
        this.cache.set(data, result);
        return result;
    }
}

module.exports = { fibonacci, DataProcessor };
