# import required packages
import cyvcf2
import tsinfer
import time
import tsdate
import numpy as np
import pandas as pd

# two different functions with two way to infer ancestral alleles
def add_haploid_sites_asp(vcf, samples):
    pos = None
    for variant in vcf:
        if pos == variant.POS:
            raise ValueError("Duplicate positions for variant at position", pos)
        else:
            pos = variant.POS
        #if any([row[2] == False for row in variant.genotypes]):
        #    raise ValueError("Unphased genotypes for variant at position", pos)
        alleles = [variant.REF] + variant.ALT
        # filter the biallelic sites only
        if len(alleles) != 2:
            continue
        # Sort with the ancestral allele first if we have one (otherwise use REF)
        ancestral = variant.INFO.get('AA', variant.REF)
        sorted_alleles = sorted(alleles, key=lambda x: x != ancestral)
        genotypes = [g for row in variant.genotypes for g in row[0:1]]
        genotypes[:] = [0 if x==-1 else x for x in genotypes]
        samples.add_site(pos, genotypes=genotypes, alleles=sorted_alleles)

def add_haploid_sites_asp_AA(vcf, samples):
    pos = None
    for variant in vcf:
        if pos == variant.POS:
            raise ValueError("Duplicate positions for variant at position", pos)
        else:
            pos = variant.POS
        #if any([row[2] == False for row in variant.genotypes]):
        #    raise ValueError("Unphased genotypes for variant at position", pos)
        alleles = [variant.REF] + variant.ALT
        # filter the biallelic sites only
        if len(alleles) != 2:
            continue
        # Sort with the ancestral allele first if we have one (otherwise use REF)
        ancestral = variant.INFO.get('AA', variant.REF)
        sorted_alleles = sorted(alleles, key=lambda x: x != ancestral)
        genotypes = [g for row in variant.genotypes for g in row[0:1]]
        genotypes[:] = [0 if x==-1 else x for x in genotypes]
        if genotypes.count(1) > 0.5 * len(genotypes):
            sorted_alleles = sorted_alleles[::-1]
        samples.add_site(pos, genotypes=genotypes, alleles=sorted_alleles)

start_time = time.time()

with tsinfer.SampleData(path="data/output/Wenhua/test/output/final_MT.samples") as samples:
    vcf = cyvcf2.VCF('data/output/Wenhua/test/output/final_MT.vcf')
    add_haploid_sites_asp_AA(vcf, samples)

inferred_ts = tsinfer.infer(samples)

for tree in inferred_ts.trees():
    print(tree.draw(format="unicode"))
for sample_id, h in enumerate(inferred_ts.haplotypes()):
    print(sample_id, h, sep="\t")

print("Sample file created for {} samples ".format(samples.num_samples) +
  "({} individuals) ".format(samples.num_individuals) +
  "with {} variable sites.".format(samples.num_sites))

print("Inferred tree sequence: {} trees over {} Mb ({} edges)".format(
    inferred_ts.num_trees, inferred_ts.sequence_length/1e6, inferred_ts.num_edges))

elapsed_time = time.time() - start_time
print(elapsed_time)

# draw trees and save figure
#tree = ts.at(10000)
#tree.draw(path="data/output/Wenhua/test/output/tree_at_MT.svg", height=700, width=1200, node_labels = {0: 'C1', 1: 'C26', 2: 'C40', 3: 'C41', 4: 'C42', 5: 'C43', 6: 'C44', 7: 'C45', 8: 'C46', 9: 'C79'})

#with tsinfer.SampleData(path="data/output/Wenhua/test/output/final_I.samples") as samples:
#    vcf = cyvcf2.VCF('data/output/Wenhua/test/output/final_I.vcf')
#    add_haploid_sites_asp_AA(vcf, samples)
#ts = tsinfer.infer(samples)

#print("Sample file created for {} samples ".format(samples.num_samples) +
#  "({} individuals) ".format(samples.num_individuals) +
#  "with {} variable sites.".format(samples.num_sites))

# Do the inference
#ts = tsinfer.infer(samples)
#print("Inferred tree sequence: {} trees over {} Mb ({} edges)".format(
#    ts.num_trees, ts.sequence_length/1e6, ts.num_edges))
#tree = ts.at(3000000)
#tree.draw(path="data/output/Wenhua/test/output/tree_at_I_3000000.svg", height=700, width=1200, node_labels = {0: 'C1', 1: 'C26', 2: 'C40', 3: 'C41', 4: 'C42', 5: 'C43', 6: 'C44', 7: 'C45', 8: 'C46', 9: 'C79'})
#tree = ts.at(4000000)
#tree.draw(path="data/output/Wenhua/test/output/tree_at_I_4000000.svg", height=700, width=1200, node_labels = {0: 'C1', 1: 'C26', 2: 'C40', 3: 'C41', 4: 'C42', 5: 'C43', 6: 'C44', 7: 'C45', 8: 'C46', 9: 'C79'})


#tree = inferred_ts.at(10000)
#tree.draw(path="data/output/Wenhua/test/output/tree_final_I_10000.svg", height = 700, width =3000, node_labels = {0: 'ARAF001', 1: 'ARAF002', 2: 'ARAF003', 3: 'ARAF004', 4: 'ARAF005', 5: 'ARAF006', 6: 'C1', 7: 'C10', 8: 'C100', 9: 'C103', 10: 'C104', \
#                                                                                                                    11: 'C105', 12: 'C106', 13: 'C107', 14: 'C108', 15: 'C109', 16: 'C11', 17: 'C110', 18: 'C111', 19: 'C112', 20: 'C113', \
#                                                                                                                    21: 'C114', 22: 'C115', 23: 'C116', 24: 'C117', 25: 'C118', 26: 'C119', 27: 'C12', 18: 'C120', 29: 'C121', 30: 'C122', \
#                                                                                                                   31: 'C123', 32: 'C124', 33: 'C125', 34: 'C126', 35: 'C127', 36: 'C128', 37: 'C129', 38: 'C13', 39: 'C130', 40: 'C131', \
#                                                                                                                    41: 'C132', 42: 'C133', 43: 'C134', 44: 'C135', 45: 'C136', 46: 'C137', 47: 'C138', 48: 'C139', 49: 'C14', 50: 'C140', \
#                                                                                                                    51: 'C141', 52: 'C142', 53: 'C143', 54: 'C144', 55: 'C145', 56: 'C146', 57: 'C147', 58: 'C148', 59: 'C149', 60: 'C15', \
#                                                                                                                    61: 'C150', 62: 'C151', 63: 'C152', 64: 'C153', 65: 'C154', 66: 'C155', 67: 'C156', 68: 'C157', 69: 'C158', 70: 'C159', \
#                                                                                                                    71: 'C16', 72: 'C160', 73: 'C161', 74: 'C162', 75: 'C163', 76: 'C164', 77: 'C165', 78: 'C166', 79: 'C167', 80: 'C168', \
#                                                                                                                    81: 'C169', 82: 'C17', 83: 'C170', 84: 'C171', 85: 'C172', 86: 'C173', 87: 'C174', 88: 'C175', 89: 'C176', 90: 'C177', \
#                                                                                                                    91: 'C178', 92: 'C179', 93: 'C18', 94: 'C180', 95: 'C181', 96: 'C182', 97: 'C183', 98: 'C184', 99: 'C185', 100: 'C186', \
#                                                                                                                    101: 'C187', 102: 'C188', 103: 'C189', 104: 'C19', 105: 'C190', 106: 'C191', 107: 'C2', 108: 'C20', 109: 'C21', 110: 'C22', \
#                                                                                                                   111: 'C220', 112: 'C221', 113: 'C222', 114: 'C223', 115: 'C23', 116: 'C24', 117: 'C246', 118: 'C25', 119: 'C26', 120: 'C27', \
#                                                                                                                    121: 'C272', 122: 'C275', 123: 'C28', 124: 'C29', 125: 'C3', 126: 'C30', 127: 'C31', 128: 'C32', 129: 'C33', 130: 'C34', \
#                                                                                                                    131: 'C341', 132: 'C342', 133: 'C343', 134: 'C344', 135: 'C345', 136: 'C346', 137: 'C35', 138: 'C354', 139: 'C355', 140: 'C356', \
#                                                                                                                    141: 'C357', 142: 'C358', 143: 'C359', 144: 'C36', 145: 'C360', 146: 'C361', 147: 'C362', 148: 'C363', 149: 'C364', 150: 'C365', \
#                                                                                                                    151: 'C366', 152: 'C367', 153: 'C368', 154: 'C369', 155: 'C37', 156: 'C38', 157: 'C39', 158: 'C4', 159: 'C40', 160: 'C41', \
#                                                                                                                    161: 'C42', 162: 'C43', 163: 'C44', 164: 'C45', 165: 'C46', 166: 'C47', 167: 'C48', 168: 'C49', 169: 'C5', 170: 'C50', \
#                                                                                                                    171: 'C51', 172: 'C52', 173: 'C53', 174: 'C54', 175: 'C55', 176: 'C56', 177: 'C57', 178: 'C58', 179: 'C59', 180: 'C6', \
#                                                                                                                   181: 'C60', 182: 'C61', 183: 'C62', 184: 'C63', 185: 'C64', 186: 'C65', 187: 'C66', 188: 'C67', 189: 'C68', 190: 'C69', \
#                                                                                                                    191: 'C7', 192: 'C70', 193: 'C71', 194: 'C72', 195: 'C73', 196: 'C74', 197: 'C75', 198: 'C76', 199: 'C77', 200: 'C78', \
#                                                                                                                    201: 'C79', 202: 'C8', 203: 'C80', 204: 'C81', 205: 'C82', 206: 'C83', 207: 'C84', 208: 'C85', 209: 'C86', 210: 'C87', \
#                                                                                                                    211: 'C88', 212: 'C89', 213: 'C91', 214: 'C92', 215: 'C93', 216: 'C95', 217: 'C96', 218: 'C99' \
#                                                                                                                    })




tsdate inferred_ts.trees dated_ts.trees 10000 -m 1e-8

import tsdate
simplets = inferred_ts.simplify()
datets = tsdate.date(simplets,Ne=10000)
# mutation_rate=1e-8

with open('testnewick.txt', 'w') as output_file:
    for tree in inferred_ts.trees():
        nw = tree.newick(
            node_labels={0: 'ARAF001', 1: 'ARAF002', 2: 'ARAF003', 3: 'ARAF004', 4: 'ARAF005', 5: 'ARAF006', 6: 'C1',
                         7: 'C10', 8: 'C100', 9: 'C103', 10: 'C104', \
                         11: 'C105', 12: 'C106', 13: 'C107', 14: 'C108', 15: 'C109', 16: 'C11', 17: 'C110', 18: 'C111',
                         19: 'C112', 20: 'C113', \
                         21: 'C114', 22: 'C115', 23: 'C116', 24: 'C117', 25: 'C118', 26: 'C119', 27: 'C12', 28: 'C120',
                         29: 'C121', 30: 'C122', \
                         31: 'C123', 32: 'C124', 33: 'C125', 34: 'C126', 35: 'C127', 36: 'C128', 37: 'C129', 38: 'C13',
                         39: 'C130', 40: 'C131', \
                         41: 'C132', 42: 'C133', 43: 'C134', 44: 'C135', 45: 'C136', 46: 'C137', 47: 'C138', 48: 'C139',
                         49: 'C14', 50: 'C140', \
                         51: 'C141', 52: 'C142', 53: 'C143', 54: 'C144', 55: 'C145', 56: 'C146', 57: 'C147', 58: 'C148',
                         59: 'C149', 60: 'C15', \
                         61: 'C150', 62: 'C151', 63: 'C152', 64: 'C153', 65: 'C154', 66: 'C155', 67: 'C156', 68: 'C157',
                         69: 'C158', 70: 'C159', \
                         71: 'C16', 72: 'C160', 73: 'C161', 74: 'C162', 75: 'C163', 76: 'C164', 77: 'C165', 78: 'C166',
                         79: 'C167', 80: 'C168', \
                         81: 'C169', 82: 'C17', 83: 'C170', 84: 'C171', 85: 'C172', 86: 'C173', 87: 'C174', 88: 'C175',
                         89: 'C176', 90: 'C177', \
                         91: 'C178', 92: 'C179', 93: 'C18', 94: 'C180', 95: 'C181', 96: 'C182', 97: 'C183', 98: 'C184',
                         99: 'C185', 100: 'C186', \
                         101: 'C187', 102: 'C188', 103: 'C189', 104: 'C19', 105: 'C190', 106: 'C191', 107: 'C2',
                         108: 'C20',
                         109: 'C21', 110: 'C22', \
                         111: 'C220', 112: 'C221', 113: 'C222', 114: 'C223', 115: 'C23', 116: 'C24', 117: 'C246',
                         118: 'C25', 119: 'C26', 120: 'C27', \
                         121: 'C272', 122: 'C275', 123: 'C28', 124: 'C29', 125: 'C3', 126: 'C30', 127: 'C31',
                         128: 'C32',
                         129: 'C33', 130: 'C34', \
                         131: 'C341', 132: 'C342', 133: 'C343', 134: 'C344', 135: 'C345', 136: 'C346', 137: 'C35',
                         138: 'C354', 139: 'C355', 140: 'C356', \
                         141: 'C357', 142: 'C358', 143: 'C359', 144: 'C36', 145: 'C360', 146: 'C361', 147: 'C362',
                         148: 'C363', 149: 'C364', 150: 'C365', \
                         151: 'C366', 152: 'C367', 153: 'C368', 154: 'C369', 155: 'C37', 156: 'C38', 157: 'C39',
                         158: 'C4',
                         159: 'C40', 160: 'C41', \
                         161: 'C42', 162: 'C43', 163: 'C44', 164: 'C45', 165: 'C46', 166: 'C47', 167: 'C48', 168: 'C49',
                         169: 'C5', 170: 'C50', \
                         171: 'C51', 172: 'C52', 173: 'C53', 174: 'C54', 175: 'C55', 176: 'C56', 177: 'C57', 178: 'C58',
                         179: 'C59', 180: 'C6', \
                         181: 'C60', 182: 'C61', 183: 'C62', 184: 'C63', 185: 'C64', 186: 'C65', 187: 'C66', 188: 'C67',
                         189: 'C68', 190: 'C69', \
                         191: 'C7', 192: 'C70', 193: 'C71', 194: 'C72', 195: 'C73', 196: 'C74', 197: 'C75', 198: 'C76',
                         199: 'C77', 200: 'C78', \
                         201: 'C79', 202: 'C8', 203: 'C80', 204: 'C81', 205: 'C82', 206: 'C83', 207: 'C84', 208: 'C85',
                         209: 'C86', 210: 'C87', \
                         211: 'C88', 212: 'C89', 213: 'C91', 214: 'C92', 215: 'C93', 216: 'C95', 217: 'C96', 218: 'C99' \
                         })
        output_file.write(nw + "\n")

with open('MT_date_1.txt', 'w') as output_file:
    for tree in datets.trees():
        nw = tree.newick(
            node_labels={0: 'ARAF001', 1: 'ARAF002', 2: 'ARAF003', 3: 'ARAF004', 4: 'ARAF005', 5: 'ARAF006', 6: 'C1',
                         7: 'C10', 8: 'C100', 9: 'C103', 10: 'C104', \
                         11: 'C105', 12: 'C106', 13: 'C107', 14: 'C108', 15: 'C109', 16: 'C11', 17: 'C110', 18: 'C111',
                         19: 'C112', 20: 'C113', \
                         21: 'C114', 22: 'C115', 23: 'C116', 24: 'C117', 25: 'C118', 26: 'C119', 27: 'C12', 28: 'C120',
                         29: 'C121', 30: 'C122', \
                         31: 'C123', 32: 'C124', 33: 'C125', 34: 'C126', 35: 'C127', 36: 'C128', 37: 'C129', 38: 'C13',
                         39: 'C130', 40: 'C131', \
                         41: 'C132', 42: 'C133', 43: 'C134', 44: 'C135', 45: 'C136', 46: 'C137', 47: 'C138', 48: 'C139',
                         49: 'C14', 50: 'C140', \
                         51: 'C141', 52: 'C142', 53: 'C143', 54: 'C144', 55: 'C145', 56: 'C146', 57: 'C147', 58: 'C148',
                         59: 'C149', 60: 'C15', \
                         61: 'C150', 62: 'C151', 63: 'C152', 64: 'C153', 65: 'C154', 66: 'C155', 67: 'C156', 68: 'C157',
                         69: 'C158', 70: 'C159', \
                         71: 'C16', 72: 'C160', 73: 'C161', 74: 'C162', 75: 'C163', 76: 'C164', 77: 'C165', 78: 'C166',
                         79: 'C167', 80: 'C168', \
                         81: 'C169', 82: 'C17', 83: 'C170', 84: 'C171', 85: 'C172', 86: 'C173', 87: 'C174', 88: 'C175',
                         89: 'C176', 90: 'C177', \
                         91: 'C178', 92: 'C179', 93: 'C18', 94: 'C180', 95: 'C181', 96: 'C182', 97: 'C183', 98: 'C184',
                         99: 'C185', 100: 'C186', \
                         101: 'C187', 102: 'C188', 103: 'C189', 104: 'C19', 105: 'C190', 106: 'C191', 107: 'C2',
                         108: 'C20',
                         109: 'C21', 110: 'C22', \
                         111: 'C220', 112: 'C221', 113: 'C222', 114: 'C223', 115: 'C23', 116: 'C24', 117: 'C246',
                         118: 'C25', 119: 'C26', 120: 'C27', \
                         121: 'C272', 122: 'C275', 123: 'C28', 124: 'C29', 125: 'C3', 126: 'C30', 127: 'C31',
                         128: 'C32',
                         129: 'C33', 130: 'C34', \
                         131: 'C341', 132: 'C342', 133: 'C343', 134: 'C344', 135: 'C345', 136: 'C346', 137: 'C35',
                         138: 'C354', 139: 'C355', 140: 'C356', \
                         141: 'C357', 142: 'C358', 143: 'C359', 144: 'C36', 145: 'C360', 146: 'C361', 147: 'C362',
                         148: 'C363', 149: 'C364', 150: 'C365', \
                         151: 'C366', 152: 'C367', 153: 'C368', 154: 'C369', 155: 'C37', 156: 'C38', 157: 'C39',
                         158: 'C4',
                         159: 'C40', 160: 'C41', \
                         161: 'C42', 162: 'C43', 163: 'C44', 164: 'C45', 165: 'C46', 166: 'C47', 167: 'C48', 168: 'C49',
                         169: 'C5', 170: 'C50', \
                         171: 'C51', 172: 'C52', 173: 'C53', 174: 'C54', 175: 'C55', 176: 'C56', 177: 'C57', 178: 'C58',
                         179: 'C59', 180: 'C6', \
                         181: 'C60', 182: 'C61', 183: 'C62', 184: 'C63', 185: 'C64', 186: 'C65', 187: 'C66', 188: 'C67',
                         189: 'C68', 190: 'C69', \
                         191: 'C7', 192: 'C70', 193: 'C71', 194: 'C72', 195: 'C73', 196: 'C74', 197: 'C75', 198: 'C76',
                         199: 'C77', 200: 'C78', \
                         201: 'C79', 202: 'C8', 203: 'C80', 204: 'C81', 205: 'C82', 206: 'C83', 207: 'C84', 208: 'C85',
                         209: 'C86', 210: 'C87', \
                         211: 'C88', 212: 'C89', 213: 'C91', 214: 'C92', 215: 'C93', 216: 'C95', 217: 'C96', 218: 'C99' \
                         })
        output_file.write(nw + "\n")

# discover GNN methods
import pandas as pd
import numpy as np
d = [[x] for x in range(219)]
GNN = inferred_ts.genealogical_nearest_neighbours(focal = range(219), sample_sets = d)
np.savetxt("GNN.csv", GNN, delimiter=",")


# add metadata information
import json

def add_populations(vcf, samples):
    """
    Add tsinfer Population objects and returns a list of IDs corresponding to the VCF samples.
    """
    # In this VCF, the first letter of the sample name refers to the population
    samples_first_letter = [sample_name[0] for sample_name in vcf.samples]
    pop_lookup = {}
    pop_lookup['8'] = samples.add_population(metadata={'country': 'Norway'})
    pop_lookup['F'] = samples.add_population(metadata={'country': 'France'})
    print(pop_lookup)
    return [pop_lookup[first_letter] for first_letter in samples_first_letter]

def chromosome_length_MT(vcf):
    return vcf.seqlens[0]

def chromosome_length_I(vcf):
    return vcf.seqlens[8]


def add_haploid_individuals(vcf, samples, populations):
    for name, population in zip(vcf.samples, populations):
        samples.add_individual(ploidy=1, metadata={"name": name}, population=population)

# Repeat as previously but add both populations and individuals
with tsinfer.SampleData(path="data/output/Wenhua/test/output/final_I.samples",
                        sequence_length=chromosome_length_I(vcf)) as samples:
    vcf = cyvcf2.VCF('data/output/Wenhua/test/output/final_I.vcf')
    # samples.add_population(metadata={'AMR': 'TR34/L98H'})
    # samples.add_population(metadata={'AMR': 'Wildtype'})
    # samples.add_population(metadata={'AMR': 'G54R'})
    # samples.add_population(metadata={'AMR': 'TR46/Y121F/T289A'})
    # samples.add_population(metadata={'AMR': 'TR34'})
    # samples.add_population(metadata={'AMR': 'TR34/L98H/T289A/I364V/G448S'})
    # samples.add_population(metadata={'AMR': 'G54W'})
    # samples.add_population(metadata={'AMR': 'G54E'})
    # samples.add_population(metadata={'AMR': 'P216L'})
    # samples.add_population(metadata={'AMR': 'NA'})
    # AMRpopulations = [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0,
    #                   0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    #                   0, 0, 9, 1, 1, 0, 0, 2, 7, 0,
    #                   0, 6, 0, 6, 1, 1, 1, 0, 6, 6,
    #                   6, 0, 0, 6, 1, 1, 8, 1, 0, 6,
    #                   0, 6, 0, 0, 8, 1, 1, 1, 0, 0,
    #                   0, 0, 1, 1, 1, 5, 5, 5, 5, 0,
    #                   0, 0, 0, 1, 6, 1, 1, 1, 1, 1,
    #                   1, 0, 1, 0, 1, 1, 1, 1, 1, 1,
    #                   1, 1, 0, 1, 1, 1, 1, 1, 1, 1,
    #                   1, 1, 2, 0, 1, 1, 0, 0, 0, 0,
    #                   1, 1, 1, 1, 0, 0, 1, 0, 2, 0,
    #                   1, 1, 0, 0, 0, 0, 0, 0, 0, 1,
    #                   0, 0, 1, 1, 1, 1, 1, 0, 0, 0,
    #                   0, 3, 0, 1, 3, 1, 1, 1, 0, 4,
    #                   0, 1, 0, 0, 1, 1, 1, 1, 1, 1,
    #                   1, 1, 1, 1, 1, 1, 1, 1, 0, 1,
    #                   1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    #                   1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
    #                   0, 0, 1, 1, 1, 1, 1, 1, 1, 0,
    #                   3, 0, 0, 1, 0, 0, 0, 0, 0, 3,
    #                   0, 3, 3, 0, 3, 1, 1, 0]
    #
    # samples.add_population(metadata={'AMR': 'TR34'})
    # samples.add_population(metadata={'AMR': 'Wildtype'})
    # samples.add_population(metadata={'AMR': 'G54'})
    # samples.add_population(metadata={'AMR': 'TR46'})
    # samples.add_population(metadata={'AMR': 'Else'})
    # AMRpopulations2 = [0 if i == 4 else i for i in AMRpopulations]
    # AMRpopulations2 = [0 if i == 5 else i for i in AMRpopulations2]
    # AMRpopulations2 = [2 if i == 6 else i for i in AMRpopulations2]
    # AMRpopulations2 = [2 if i == 7 else i for i in AMRpopulations2]
    # AMRpopulations2 = [4 if i == 8 else i for i in AMRpopulations2]
    # AMRpopulations2 = [4 if i == 9 else i for i in AMRpopulations2]

    # samples.add_population(metadata={'DAPCcluster': '1'})
    # samples.add_population(metadata={'DAPCcluster': '2'})
    # samples.add_population(metadata={'DAPCcluster': '3'})
    # samples.add_population(metadata={'DAPCcluster': 'NA'})
    # DAPCpopulations = [0, 0, 1, 0, 1, 0, 2, 0, 2, 2, 2,
    #                   0, 0, 0, 2, 1, 0, 2, 1, 2, 1,
    #                   2, 2, 3, 1, 1, 2, 2, 1, 0, 0,
    #                   2, 1, 2, 1, 1, 1, 1, 0, 1, 1,
    #                   1, 2, 1, 1, 1, 1, 1, 1, 0, 1,
    #                   1, 0, 2, 0, 1, 1, 1, 1, 0, 0,
    #                   0, 0, 1, 1, 1, 0, 0, 0, 0, 0,
    #                   2, 0, 2, 0, 0, 1, 1, 1, 1, 1,
    #                   1, 2, 1, 0, 1, 1, 1, 1, 1, 0,
    #                   1, 1, 2, 1, 1, 1, 1, 1, 1, 0,
    #                   1, 0, 1, 0, 1, 1, 0, 2, 2, 2,
    #                   0, 0, 1, 0, 2, 2, 0, 0, 0, 0,
    #                   1, 1, 0, 0, 2, 0, 2, 2, 2, 1,
    #                   0, 0, 1, 1, 1, 1, 0, 2, 2, 0,
    #                   2, 0, 0, 0, 0, 1, 0, 1, 0, 0,
    #                   0, 1, 2, 0, 1, 0, 1, 1, 1, 1,
    #                   1, 1, 1, 1, 1, 1, 1, 1, 2, 1,
    #                   1, 1, 1, 1, 1, 1, 1, 0, 0, 0,
    #                   0, 0, 0, 0, 0, 0, 0, 1, 2, 2,
    #                   0, 2, 1, 1, 1, 1, 0, 1, 1, 2,
    #                   0, 2, 0, 1, 0, 2, 2, 0, 0, 1,
    #                   0, 0, 1, 0, 0, 1, 1, 0]

    # samples.add_population(metadata={'Year': '2005'})
    # samples.add_population(metadata={'Year': '2009'})
    # samples.add_population(metadata={'Year': '2010'})
    # samples.add_population(metadata={'Year': '2011'})
    # samples.add_population(metadata={'Year': '2012'})
    # samples.add_population(metadata={'Year': '2013'})
    # samples.add_population(metadata={'Year': '2014'})
    # samples.add_population(metadata={'Year': '2015'})
    # samples.add_population(metadata={'Year': '2016'})
    # samples.add_population(metadata={'Year': '2017'})
    # samples.add_population(metadata={'Year': 'NA'})
    Yearpopulations = [4, 4, 1, 4, 4, 4, 7, 7, 6, 7, 7,
                      7, 6, 7, 7, 7, 7, 7, 8, 8, 8,
                      7, 9, 10, 8, 8, 7, 7, 8, 7, 7,
                      8, 7, 7, 7, 7, 7, 7, 7, 7, 7,
                      7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
                      7, 7, 7, 7, 7, 1, 1, 1, 1, 7,
                      1, 1, 1, 1, 1, 8, 8, 8, 8, 8,
                      7, 8, 9, 7, 7, 7, 6, 7, 7, 8,
                      7, 7, 7, 7, 8, 7, 7, 8, 8, 7,
                      7, 7, 7, 7, 7, 7, 7, 7, 7, 8,
                      6, 6, 6, 7, 6, 7, 7, 7, 7, 7,
                      0, 0, 0, 0, 7, 7, 4, 7, 7, 7,
                      4, 2, 7, 7, 7, 7, 7, 5, 7, 7,
                      9, 9, 9, 9, 9, 9, 5, 10, 10, 10,
                      10, 10, 10, 5, 10, 10, 10, 10, 8, 8,
                      8, 8, 8, 8, 6, 6, 6, 7, 5, 3,
                      3, 3, 3, 3, 3, 3, 3, 4, 7, 4,
                      5, 4, 4, 4, 5, 2, 2, 4, 5, 7,
                      5, 5, 5, 5, 5, 2, 2, 2, 5, 10,
                      7, 10, 3, 3, 3, 3, 10, 3, 3, 6,
                      6, 7, 6, 7, 7, 7, 7, 8, 8, 7,
                      7, 7, 7, 7, 7, 7, 7, 5]
    # samples.add_population(metadata={'Year': '2005'})
    # samples.add_population(metadata={'Year': '2009'})
    # samples.add_population(metadata={'Year': '2010'})
    # samples.add_population(metadata={'Year': '2011'})
    # samples.add_population(metadata={'Year': '2012'})
    # samples.add_population(metadata={'Year': '2013'})
    # samples.add_population(metadata={'Year': '2014'})
    # samples.add_population(metadata={'Year': '2015'})
    # samples.add_population(metadata={'Year': '2016'})
    # samples.add_population(metadata={'Year': '2017'})
    samples.add_population(metadata={'Year': '2005-2011'})
    samples.add_population(metadata={'Year': '2012-2014'})
    samples.add_population(metadata={'Year': '2015'})
    samples.add_population(metadata={'Year': '2016-2017'})
    samples.add_population(metadata={'Year': 'Else'})
    Yearpopulations2 = [0 if i == 1 else i for i in Yearpopulations]
    Yearpopulations2 = [0 if i == 2 else i for i in Yearpopulations2]
    Yearpopulations2 = [0 if i == 3 else i for i in Yearpopulations2]
    Yearpopulations2 = [1 if i == 4 else i for i in Yearpopulations2]
    Yearpopulations2 = [1 if i == 5 else i for i in Yearpopulations2]
    Yearpopulations2 = [1 if i == 6 else i for i in Yearpopulations2]
    Yearpopulations2 = [2 if i == 7 else i for i in Yearpopulations2]
    Yearpopulations2 = [3 if i == 8 else i for i in Yearpopulations2]
    Yearpopulations2 = [3 if i == 9 else i for i in Yearpopulations2]
    Yearpopulations2 = [4 if i == 10 else i for i in Yearpopulations2]

    #populations = add_populations(vcf, samples)
    #add_haploid_individuals(vcf, samples, AMRpopulations)
    #add_haploid_individuals(vcf, samples, AMRpopulations2)
    #add_haploid_individuals(vcf, samples, DAPCpopulations)
    #add_haploid_individuals(vcf, samples, Yearpopulations)
    add_haploid_individuals(vcf, samples, Yearpopulations2)
    add_haploid_sites_asp(vcf, samples)

# Do the inference
sparrow_ts = tsinfer.infer(samples)
print("Inferred tree sequence `{}`: {} trees over {} Mb".format(
    "sparrow_ts", sparrow_ts.num_trees, sparrow_ts.sequence_length/1e6))
# Check the metadata
#for sample_node_id in sparrow_ts.samples():
#    individual_id = sparrow_ts.node(sample_node_id).individual
#    population_id = sparrow_ts.node(sample_node_id).population
#    print(
#         "Node", sample_node_id, "labels one whole genome aspergillus",
#         json.loads(sparrow_ts.individual(individual_id).metadata),
#         "in", json.loads(sparrow_ts.population(population_id).metadata)['AMR'])

samples_listed_by_population = [sparrow_ts.samples(population=pop_id)
    for pop_id in range(sparrow_ts.num_populations)]


gnn = sparrow_ts.genealogical_nearest_neighbours(
    sparrow_ts.samples(), samples_listed_by_population)

# Tabulate GNN nicely using a Pandas dataframe with named rows and columns
sample_nodes = [sparrow_ts.node(n) for n in sparrow_ts.samples()]
sample_ids = [n.id for n in sample_nodes]
sample_names = [json.loads(sparrow_ts.individual(n.individual).metadata)['name'] for n in sample_nodes]

#sample_pops = [json.loads(sparrow_ts.population(n.population).metadata)['AMR'] for n in sample_nodes]
#sample_pops = [json.loads(sparrow_ts.population(n.population).metadata)['DAPCcluster'] for n in sample_nodes]
sample_pops = [json.loads(sparrow_ts.population(n.population).metadata)['Year'] for n in sample_nodes]

gnn_table = pd.DataFrame(
    data=gnn,
    index=[pd.Index(sample_ids, name="Sample node"),
           pd.Index(sample_names, name="Bird"),
           #pd.Index(sample_pops, name="AMR")
           #pd.Index(sample_pops, name="DAPCcluster")
           pd.Index(sample_pops, name="Year")
           ],
    #columns=[json.loads(p.metadata)['AMR'] for p in sparrow_ts.populations()])
    #columns=[json.loads(p.metadata)['DAPCcluster'] for p in sparrow_ts.populations()])
    columns=[json.loads(p.metadata)['Year'] for p in sparrow_ts.populations()])

print(gnn_table)

# Summarize GNN for all birds from the same country
#print(gnn_table.groupby(level="AMR").mean())
#print(gnn_table.groupby(level="DAPCcluster").mean())
#print(gnn_table.groupby(level="Year").mean())
Yearchr1 = gnn_table.groupby(level="Year").mean()
