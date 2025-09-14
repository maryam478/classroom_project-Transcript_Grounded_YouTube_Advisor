from pipeline import ask

def test_schema():
    ans = ask("How do I improve my intros?")
    assert "[source:" in ans

def test_grounding():
    ans = ask("What storytelling tips does Hayden give?")
    assert "hayden" in ans.lower()

def test_fallback():
    ans = ask("How to enable Adsense?")
    assert "not covered" in ans.lower()
