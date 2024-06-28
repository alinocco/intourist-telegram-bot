from model_utils import Choices

COMPLEXITY_CHOICES = (
    ('light', 'Лёгкий'),
    ('medium', 'Средний'),
    ('hard', 'Сложный'),
)

TOUR_INSTANCE_STATUSES = Choices(
    ('pending', 'Набор пока не открыт'),
    ('open', 'Набор открыт'),
    ('closed', 'Набор закрыт'),
    ('cancelled', 'Отменён'),
)
