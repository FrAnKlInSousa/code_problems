from src.code_problems.code_wars.kyu_6.the_lamp_revisited import Lamp


def test_the_lamp_revisited_should_return_default_values():
    lamp = Lamp('Blue')
    assert lamp.on == False
    assert lamp.color == 'Blue'
    assert lamp.state() == 'The lamp is off.'

def test_switch_the_lamp_revisited():
    lamp = Lamp('Blue')
    lamp.toggle_switch()
    assert lamp.on
    assert lamp.state() == 'The lamp is on.'