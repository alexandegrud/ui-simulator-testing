
def test_sort_name_column(init_sorting_page):
    init_sorting_page.open_section()
    init_sorting_page.set_name_sort(True)
    init_sorting_page.assertions.is_text_sorted(init_sorting_page.get_column(get_name_column=True))

def test_sort_age(init_sorting_page):
    init_sorting_page.open_section()
    init_sorting_page.set_age_sort(True)
    init_sorting_page.assertions.are_digits_sorted(init_sorting_page.get_column(get_age_column=True))

def test_sort_role(init_sorting_page):
    init_sorting_page.open_section()
    init_sorting_page.set_role_sort(True)
    init_sorting_page.assertions.is_text_sorted(init_sorting_page.get_column(get_role_column=True))


