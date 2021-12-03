from day2.day2 import *


class TestSubmarine:
    def setup_method(self, method):
        self.submarine = Submarine()

    def test_init(self):
        assert self.submarine.horizontal == 0
        assert self.submarine.depth == 0
        assert self.submarine.aim == 0

    def test_process_instruction_when_forward1_expect_horizonatal1_depth0(self):
        self.submarine.process_instruction(Instruction("forward", 1))

        assert self.submarine.horizontal == 1
        assert self.submarine.depth == 0

    def test_process_instruction_when_down2_forward1_expect_horizonatal1_depth2(self):
        self.submarine.process_instruction(Instruction("down", 2))
        self.submarine.process_instruction(Instruction("forward", 1))

        assert self.submarine.horizontal == 1
        assert self.submarine.depth == 2

    def test_process_instruction_when_down2_forward1_up_1_forward2_expect_horizonatal1_depth1(
        self,
    ):
        self.submarine.process_instruction(Instruction("down", 2))
        self.submarine.process_instruction(Instruction("forward", 1))
        self.submarine.process_instruction(Instruction("up", 1))
        self.submarine.process_instruction(Instruction("forward", 2))

        assert self.submarine.horizontal == 3
        assert self.submarine.depth == 4

    def test_process_instruction_sample_scenario(self):
        self.submarine.process_instruction(Instruction("forward", 5))
        self.submarine.process_instruction(Instruction("down", 5))
        self.submarine.process_instruction(Instruction("forward", 8))
        self.submarine.process_instruction(Instruction("up", 3))
        self.submarine.process_instruction(Instruction("down", 8))
        self.submarine.process_instruction(Instruction("forward", 2))

        assert self.submarine.horizontal == 15
        assert self.submarine.depth == 60
