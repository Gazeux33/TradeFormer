


class CombinedDataLoader:
    def __init__(self, *dataloaders) -> None:
        self.dataloaders = dataloaders
        self.iterators = [iter(dl) for dl in dataloaders]

    def __iter__(self) -> 'CombinedDataLoader':
        self.iterators = [iter(dl) for dl in self.dataloaders]
        return self

    def __next__(self) -> tuple:
        for it in self.iterators:
            try:
                return next(it)
            except StopIteration:
                self.iterators.remove(it)
                if not self.iterators:
                    raise StopIteration
        raise StopIteration

    def __len__(self) -> int:
        return sum(len(dl) for dl in self.dataloaders)


