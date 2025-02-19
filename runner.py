import subprocess


test_files = ['test0_smoke.py',
              'test1_ab_testing.py',
              'test2_add_remove_elements.py',
              'test3_basic_auth.py',
              'test4_broken_images.py',
              'test5_challenging_dom.py',
              'test6_checkboxes.py',
              'test7_context_menu.py',
              'test8_digest_authentication',
              'test9_disappearing_elements',
              'test10_drag_and_drop',
              'test11_dropdown',
              'test12_dynamic_content.py']


if __name__ == '__main__':
    for test in test_files:
        result = subprocess.run(['python', test], capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)
        