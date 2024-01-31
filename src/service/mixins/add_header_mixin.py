class HeaderMixin:
    def add_header(self, header_list: list):
        member_name = "member_name"
        member_surname = "member_surname"

        if member_name in self.request.POST.keys() and member_surname in self.request.POST.keys():
            header_list.append("Imię drugiego uczęstnika")
            header_list.append("Nazwisko drugiego uczęstnika")

        elif member_name in self.request.POST.keys():
            header_list.append("Imię drugiego uczęstnika")

        else:
            header_list.append("Nazwisko drugiego uczęstnika")