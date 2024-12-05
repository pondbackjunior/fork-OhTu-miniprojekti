

class Booklet:
    def __init__(
        self,
        ref_id,
        authors,
        title,
        howpublished,
        address,
        year,
        editor=None,
        volume=None,
        number=None,
        organization=None,
        month=None,
        note=None,
    ):
        self.id = ref_id
        self.authors = authors
        self.title = title
        self.howpublished = howpublished
        self.address = address
        self.year = year
        self.editor = editor
        self.volume = volume
        self.number = number
        self.organization = organization
        self.month = month
        self.note = note
        self.type = "booklet"
        

    @staticmethod
    def from_form(form):
        return Booklet(
            form.get("reference_id") or None,
            form.getlist("author"),
            form.get("title"),
            form.get("howpublished"),
            form.get("address"),
            form.get("year"),
            form.get("editor") or None,
            form.get("volume") or None,
            form.get("number") or None,
            form.get("organization") or None,
            form.get("month") or None,
            form.get("note") or None,
        )

    def __str__(self):
        editor = None
        vol = None
        no = None
        month = None
        note = None

        if self.editor:
            editor = f"editor: {self.editor}."
        if self.volume:
            vol = f"vol. {self.volume}."
        if self.number:
            no = f"no. {self.number}."
        if self.organization:
            org = f"organization: {self.organization}."
        if self.month:
            month = f"month: {self.month}."
        if self.note:
            note = f"notes: {self.note}."
        return f"{self.authors}. {self.title}. {self.howpublished}, {self.address}, {self.year}. {editor or ''} {vol or ''} {no or ''} {org or ''}{month or ''} {note or ''}"