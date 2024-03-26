class CSVData:
    def __init__(self, game_creation, queue_id):
        self.game_creation = game_creation
        if queue_id is 400:
            self.game_mode = "Normal Draft"
        if queue_id is 420:
            self.game_mode = "Ranked Solo/Duo"
        if queue_id is 440:
            self.game_mode = "Ranked Flex"
