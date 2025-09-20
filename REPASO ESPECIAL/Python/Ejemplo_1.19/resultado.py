class Prescription:
    def __init__(self, drug_name, dosage_mg, is_active=True):
        self.drug_name = drug_name
        self.dosage_mg = dosage_mg
        self.is_active = is_active

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class PatientLogBase:
    def __init__(self):
        self.first = None
        self._size = 0

    def add_prescription(self, prescription):
        new_node = Node(prescription)
        if self.first is None: self.first = new_node
        else:
            curr = self.first
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self._size += 1

    def get_size(self):
        return self._size

class PatientLog(PatientLogBase):
    total_prescriptions_issued = 0
    
    def add_prescription(self, prescription):
        super().add_prescription(prescription)
        PatientLog.total_prescriptions_issued += 1

    def deactivate_prescription(self, drug_name):
        curr = self.first
        while curr:
            if curr.value.drug_name == drug_name:
                curr.value.is_active = False
                return True
            curr = curr.next
        return False

    @property
    def active_prescriptions_count(self):
        count = 0
        curr = self.first
        while curr:
            if curr.value.is_active:
                count += 1
            curr = curr.next
        return count

    def get_active_drugs(self):
        drugs = []
        curr = self.first
        while curr:
            if curr.value.is_active:
                drugs.append(curr.value.drug_name)
            curr = curr.next
        return drugs