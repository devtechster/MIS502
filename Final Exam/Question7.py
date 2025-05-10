import pandas as pd
chunk_size = 3000
batch_num = 1

# initialize CSV output file
csv_out_file = 'question7output.csv'

for chunk in pd.read_csv('SchData2013.csv', chunksize=chunk_size, iterator=True):

    # filter for SurgicalArea and SurgicalSpecialty
    filtered_chunk = chunk[(chunk['SurgicalArea'] == 'CVOR') | (chunk['SurgicalSpecialty'] == 'CV')]

    # slice and dice the filtered chunk
    sliced_chunk = filtered_chunk[['SurgicalArea', 'SurgicalSpecialty', 'SSSNo', 'PatientAge',
                                   'TotalSurgeryMin', 'PrimaryProcedure', 'OperatingRoom']]

    # write the sliced and diced chunk to CSV
    if batch_num == 1:
        sliced_chunk.to_csv(csv_out_file, header=True, index=False)
    else:
        sliced_chunk.to_csv(csv_out_file, mode='a', header=False, index=False)

    print(f'Chunk {batch_num} written to CSV. Type: {type(sliced_chunk)}')
    batch_num += 1

print(chunk.head())
print(filtered_chunk.head())
print(sliced_chunk.head())