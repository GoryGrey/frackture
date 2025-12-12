import pytest
import numpy as np


@pytest.fixture
def sample_text():
    return "Hello, world! This is a test string with UTF-8 characters: 你好世界 🌍"


@pytest.fixture
def sample_bytes():
    return b"Binary data with various bytes: \x00\x01\x02\xff\xfe\xfd"


@pytest.fixture
def sample_dict():
    return {
        "key1": "value1",
        "key2": 42,
        "key3": [1, 2, 3],
        "nested": {"inner": "data"}
    }


@pytest.fixture
def sample_list():
    return [1.0, 2.5, 3.7, 4.2, 5.9, 6.1, 7.3, 8.8, 9.4, 10.0]


@pytest.fixture
def sample_numpy_array():
    return np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0], dtype=np.float32)


@pytest.fixture
def sample_numpy_2d_array():
    return np.random.rand(10, 10).astype(np.float32)


@pytest.fixture
def malformed_payloads():
    return [
        {},
        {"symbolic": "invalid"},
        {"entropy": "invalid"},
        {"symbolic": 123, "entropy": [1, 2, 3]},
        {"symbolic": "", "entropy": []},
        {"symbolic": "abc", "entropy": [1] * 16},
        None,
    ]


@pytest.fixture
def empty_inputs():
    return [
        "",
        b"",
        [],
        np.array([]),
        {},
    ]


@pytest.fixture
def large_inputs():
    return {
        "text": "a" * 10000,
        "bytes": b"b" * 10000,
        "array": np.random.rand(10000).astype(np.float32),
    }


@pytest.fixture
def normalized_vector():
    return np.linspace(0, 1, 768, dtype=np.float32)


@pytest.fixture
def random_vector():
    rng = np.random.default_rng(42)
    return rng.random(768, dtype=np.float32)
