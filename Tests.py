import cesar

def test_basic_shift():
    #"abc" -> "def"
    encrypted = cesar.cifrar(3, "abc")
    assert encrypted == "def", f"Expected 'def', but got '{encrypted}'"
    
    decrypted = cesar.descifrar(3, "def")
    assert decrypted == "abc", f"Expected 'abc', but got '{decrypted}'"
    print("Test 1 Passed: Basic Shift")

def test_alphabet_wrap_around():
    #"xyz" -> "cde"
    encrypted = cesar.cifrar(5, "xyz")
    assert encrypted == "cde", f"Expected 'cde', but got {encrypted}"
    
    decrypted = cesar.descifrar(5, "cde")
    assert decrypted == "xyz", f"Expected 'xyz', but got '{decrypted}'"
    print("Test 2 Passed: Alphabet Wrap-Around")

def test_case_preservation():
    #"Hello World" -> "Khoor Zruog"
    encrypted = cesar.cifrar(3, "Hello World")
    assert encrypted == "Khoor Zruog", f"Expected 'Khoor Zruog', but got '{encrypted}'"
    
    decrypted = cesar.descifrar(3, "Khoor Zruog")
    assert decrypted == "Hello World", f"Expected 'Hello World', but got '{decrypted}'"
    print("Test 3 Passed: Case Preservation")

def test_punctuation_and_numbers():
    #"python 3.10 is great, right?!" -> "wfaovu 3.10 pz nylha, ypnoa?!"
    original_text = "python 3.10 is great, right?!"
    encrypted = cesar.cifrar(7, original_text)
    
    expected = "wfaovu 3.10 pz nylha, ypnoa?!"
    assert encrypted == expected, f"Expected '{expected}', but got '{encrypted}'"
    
    decrypted = cesar.descifrar(7, expected)
    assert decrypted == original_text, f"Expected '{original_text}', but got '{decrypted}'"
    print("Test 4 Passed: Non-Alphabet Characters")

def test_large_key():
    #"hello" -> "ifmmp" saltando por 27
    encrypted = cesar.cifrar(27, "hello")
    assert encrypted == "ifmmp", f"Expected 'ifmmp', but got '{encrypted}'"
    
    decrypted = cesar.descifrar(27, "ifmmp")
    assert decrypted == "hello", f"Expected 'hello', but got '{decrypted}'"
    print("Test 5 Passed: Large Key Modulo")

# Run all tests
if __name__ == "__main__":
    print("Running Caesar Cipher Tests...\n" + "-"*30)
    test_basic_shift()
    test_alphabet_wrap_around()
    test_case_preservation()
    test_punctuation_and_numbers()
    test_large_key()
    print("-" * 30 + "\nAll tests passed successfully!")