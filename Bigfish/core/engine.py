"""
策略执行引擎,相当于发动机,负责启动一个策略,每个用户(或者组)都可以有一个引擎
"""


class Engine:
    def __init__(self):
        pass

    def submit(self, strategy, config):
        """
        提交一个策略进行执行
        :param strategy: Strategy实例
        :param config: Config实例, 执行策略所需要的配置
        """
        pass
