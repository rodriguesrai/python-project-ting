from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    PQ = PriorityQueue()
    assert len(PQ) == 0

    PQ.enqueue({"qtd_linhas": 8})
    PQ.enqueue({"qtd_linhas": 3})
    PQ.enqueue({"qtd_linhas": 2})
    assert len(PQ.regular_priority) == 1
    assert len(PQ.high_priority) == 2

    PQ.dequeue()
    assert len(PQ.high_priority) == 1

    teste = PQ.search(0)
    assert teste["qtd_linhas"] == 2

    with pytest.raises(IndexError):
        PQ.search(5)
