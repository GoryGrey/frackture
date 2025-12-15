import pytest

from benchmarks.analyze_results import analyze_vs_gzip_brotli


@pytest.fixture
def sample_competition_results():
    # Minimal benchmark JSON-like structure (data['results'] contents)
    return {
        "text_plain_medium": [
            {
                "name": "Frackture",
                "success": True,
                "tier_name": "medium",
                "category_name": "text",
                "compression_ratio": 1000.0,
                "encode_throughput": 50.0,
                "original_size": 102400,
            },
            {
                "name": "Gzip L1",
                "success": True,
                "tier_name": "medium",
                "gzip_level": 1,
                "compression_ratio": 3.0,
                "encode_throughput": 60.0,
            },
            {
                "name": "Gzip L9",
                "success": True,
                "tier_name": "medium",
                "gzip_level": 9,
                "compression_ratio": 4.0,
                "encode_throughput": 40.0,
            },
            {
                "name": "Brotli Q6",
                "success": True,
                "tier_name": "medium",
                "brotli_quality": 6,
                "compression_ratio": 5.0,
                "encode_throughput": 20.0,
            },
        ],
        "binary_png_tiny": [
            {
                "name": "Frackture",
                "success": True,
                "tier_name": "tiny",
                "category_name": "binary",
                "compression_ratio": 0.5,
                "encode_throughput": 30.0,
                "original_size": 50,
            },
            {
                "name": "Gzip L1",
                "success": True,
                "tier_name": "tiny",
                "gzip_level": 1,
                "compression_ratio": 0.8,
                "encode_throughput": 25.0,
            },
            {
                "name": "Brotli Q6",
                "success": True,
                "tier_name": "tiny",
                "brotli_quality": 6,
                "compression_ratio": 0.9,
                "encode_throughput": 10.0,
            },
        ],
    }


def test_analyze_vs_gzip_brotli_counts(sample_competition_results):
    summary = analyze_vs_gzip_brotli(sample_competition_results)

    assert summary["total_comparisons"] == 5
    assert summary["frackture_wins_ratio"] == 3
    assert summary["frackture_wins_speed"] == 4

    assert summary["gzip_by_level"]
    assert summary["brotli_by_quality"]

    # Gzip L1 comparisons: 2 datasets, Frackture wins ratio only on the medium tier
    assert summary["gzip_by_level"]["1"]["total_comparisons"] == 2
    assert summary["gzip_by_level"]["1"]["frackture_wins_ratio"] == 1

    # Brotli Q6 comparisons: 2 datasets, Frackture wins ratio only on the medium tier
    assert summary["brotli_by_quality"]["6"]["total_comparisons"] == 2
    assert summary["brotli_by_quality"]["6"]["frackture_wins_ratio"] == 1


def test_analyze_vs_gzip_brotli_by_tier(sample_competition_results):
    summary = analyze_vs_gzip_brotli(sample_competition_results)

    assert "by_tier" in summary
    assert set(summary["by_tier"].keys()) >= {"medium", "tiny"}

    assert summary["by_tier"]["medium"]["total_comparisons"] == 3
    assert summary["by_tier"]["medium"]["frackture_wins_ratio"] == 3
    assert summary["by_tier"]["medium"]["win_rate_ratio"] == pytest.approx(1.0)

    assert summary["by_tier"]["tiny"]["total_comparisons"] == 2
    assert summary["by_tier"]["tiny"]["frackture_wins_ratio"] == 0
    assert summary["by_tier"]["tiny"]["win_rate_ratio"] == pytest.approx(0.0)
