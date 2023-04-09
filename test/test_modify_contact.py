from model.contact import  Contact

def test_modify_contact_firstname(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Changed firstname3", lastname="Changed lastname3")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    #print("old contacts: ", old_contacts)
    #print("new contacts: ", new_contacts)
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)