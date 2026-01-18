from cube import cube_calculator
def test_cube_calculator():
    excepted_output = (
        "Enter a number: 2 \n"
        "cube = num ** 3\n"
        "print(f\"Cube of {num} is {cube}\")\n"
    )
    assert cube_calculator.main("2") == excepted_output