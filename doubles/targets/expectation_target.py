from doubles.lifecycle import current_space


def expect(target):
    return ExpectationTarget(target)


class ExpectationTarget(object):
    def __init__(self, target):
        self._proxy = current_space().proxy_for(target)

    def to_receive(self, method_name):
        self._proxy.add_expectation(method_name)