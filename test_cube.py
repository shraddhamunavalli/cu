from program import cube
def test_cube():
    excepted_output = (
        "Enter a number: 2 \n"
        "cube = num ** 3\n"
        "print(f\"Cube of {num} is {cube}\")\n"
    )
    assert cube.main("2") == excepted_output
