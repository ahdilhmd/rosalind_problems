
class DNA_To_RNA:
    def convert_dna_to_rna(self, dna_string):
        rna_string = ""
        dna_list = [char for char in dna_string]
        for i in range(len(dna_list)):
            if dna_list[i] == 'T':
                dna_list[i] = 'U'
        for char in dna_list:
            rna_string += char
        
        return rna_string

dna_string = "GATGGAACTTGACTACGTAAATT"
dna_to_rna = DNA_To_RNA()
dna_to_rna.convert_dna_to_rna(dna_string)
