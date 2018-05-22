from rolepermissions.roles import AbstractUserRole

class Faculty(AbstractUserRole):
    available_permissions = {
        'notes.add_note': True,
        'notes.change_note': True,
        'notes.delete_note': True,
        'notes.view_notes_ui': True,
    }
class ZenStudent(AbstractUserRole):
    available_permissions = {
        'notes.view_notes_ui': True,
    }
class AuthenticatedUser(AbstractUserRole):
    available_permissions = {
        'notes.view_notes_ui': True,
    }
class PaidUser(AbstractUserRole):
    available_permissions = {
        'notes.view_notes_ui': True,
    }