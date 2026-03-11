# Evaluation and Testing Script

# Sample function to evaluate

def sample_function(x):
    return x * 2

# Test the sample function

def test_sample_function():
    assert sample_function(2) == 4, "Test failed!"
    assert sample_function(3) == 6, "Test failed!"
    print("All tests passed!")

if __name__ == '__main__':
    test_sample_function()