def test_exercise_1_lists(tb):
    books = tb.ref("books")

    assert "The Pragmatic Programmer" in books
    assert "Clean Code" in books
    assert "Fluent Python" in books
    assert "Old Manual" not in books
    assert books == sorted(books)


RESULTS = [("Alice", 85), ("Bob", 72), ("Carol", 91)]


def test_exercise_2_tuple_unpacking(tb):
    out = tb.cell_output_text(5)

    for name, score in RESULTS:
        assert name in out
        assert str(score) in out


def test_exercise_3_sets(tb):
    workshop_a = {"Alice", "Bob", "Carol", "Dan"}
    workshop_b = {"Carol", "Dan", "Eve", "Frank"}

    assert set(tb.ref("both")) == workshop_a & workshop_b
    assert set(tb.ref("only_one")) == workshop_a ^ workshop_b
    assert tb.ref("total_unique") == len(workshop_a | workshop_b)


def test_exercise_4_dicts_and_comprehensions(tb):
    assert sorted(tb.ref("engineering_names")) == ["Alice", "Carol"]

    salary_by_department = tb.ref("salary_by_department")
    assert salary_by_department["Engineering"] == 15000
    assert salary_by_department["Sales"] == 10500
    assert salary_by_department["Marketing"] == 6000

    assert tb.ref("top_earner") == "Carol"
