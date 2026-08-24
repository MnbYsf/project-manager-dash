# from enum import Enum


# class TaskStatus(Enum):
#     planned = "planned"
#     in_progress = "in_progress"
#     done = "done"
#     blocked = "blocked"


# def is_overdue(due_date, status):
#     from datetime import date

#     if (
#         status in [TaskStatus.blocked, TaskStatus.in_progress]
#         and due_date < date.today()
#     ):
#         return True
#     return False


# def next_status(current):
#     match current:
#         case TaskStatus.planned:
#             return TaskStatus.in_progress.value
#         case TaskStatus.in_progress:
#             return TaskStatus.done.value
#         case TaskStatus.done:
#             return TaskStatus.done.value
#         case TaskStatus.blocked:
#             return TaskStatus.blocked.value


# from datetime import date, timedelta

# yesterday = date.today() - timedelta(days=1)
# if __name__ == "__main__":
#     print(is_overdue(None, TaskStatus.planned))  # False
#     print(is_overdue(yesterday, TaskStatus.done))  # False
#     print(is_overdue(yesterday, TaskStatus.in_progress))  # True

#     print(next_status(TaskStatus.planned))  # TaskStatus.in_progress
#     print(next_status(TaskStatus.in_progress))  # TaskStatus.done
#     print(next_status(TaskStatus.done))  # TaskStatus.done
#     print(next_status(TaskStatus.blocked))  # TaskStatus.blocked
