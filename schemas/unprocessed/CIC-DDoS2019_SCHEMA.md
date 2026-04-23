** `*` indicates string values present in the column 
   `†` indicates float values present in the column ** 
|    | Column                      | Types     |
|---:|:----------------------------|:----------|
|  0 | Unnamed: 0                  | int       |
|  1 | Flow ID                     | str*      |
|  2 | Source IP                   | str*      |
|  3 | Source Port                 | int       |
|  4 | Destination IP              | str*      |
|  5 | Destination Port            | int       |
|  6 | Protocol                    | int       |
|  7 | Timestamp                   | str*      |
|  8 | Flow Duration               | int       |
|  9 | Total Fwd Packets           | int       |
| 10 | Total Backward Packets      | int       |
| 11 | Total Length of Fwd Packets | float†    |
| 12 | Total Length of Bwd Packets | float†    |
| 13 | Fwd Packet Length Max       | float†    |
| 14 | Fwd Packet Length Min       | float†    |
| 15 | Fwd Packet Length Mean      | float†    |
| 16 | Fwd Packet Length Std       | float†    |
| 17 | Bwd Packet Length Max       | float†    |
| 18 | Bwd Packet Length Min       | float†    |
| 19 | Bwd Packet Length Mean      | float†    |
| 20 | Bwd Packet Length Std       | float†    |
| 21 | Flow Bytes/s                | float†    |
| 22 | Flow Packets/s              | float†    |
| 23 | Flow IAT Mean               | float†    |
| 24 | Flow IAT Std                | float†    |
| 25 | Flow IAT Max                | float†    |
| 26 | Flow IAT Min                | float†    |
| 27 | Fwd IAT Total               | float†    |
| 28 | Fwd IAT Mean                | float†    |
| 29 | Fwd IAT Std                 | float†    |
| 30 | Fwd IAT Max                 | float†    |
| 31 | Fwd IAT Min                 | float†    |
| 32 | Bwd IAT Total               | float†    |
| 33 | Bwd IAT Mean                | float†    |
| 34 | Bwd IAT Std                 | float†    |
| 35 | Bwd IAT Max                 | float†    |
| 36 | Bwd IAT Min                 | float†    |
| 37 | Fwd PSH Flags               | int       |
| 38 | Bwd PSH Flags               | int       |
| 39 | Fwd URG Flags               | int       |
| 40 | Bwd URG Flags               | int       |
| 41 | Fwd Header Length           | int       |
| 42 | Bwd Header Length           | int       |
| 43 | Fwd Packets/s               | float†    |
| 44 | Bwd Packets/s               | float†    |
| 45 | Min Packet Length           | float†    |
| 46 | Max Packet Length           | float†    |
| 47 | Packet Length Mean          | float†    |
| 48 | Packet Length Std           | float†    |
| 49 | Packet Length Variance      | float†    |
| 50 | FIN Flag Count              | int       |
| 51 | SYN Flag Count              | int       |
| 52 | RST Flag Count              | int       |
| 53 | PSH Flag Count              | int       |
| 54 | ACK Flag Count              | int       |
| 55 | URG Flag Count              | int       |
| 56 | CWE Flag Count              | int       |
| 57 | ECE Flag Count              | int       |
| 58 | Down/Up Ratio               | float†    |
| 59 | Average Packet Size         | float†    |
| 60 | Avg Fwd Segment Size        | float†    |
| 61 | Avg Bwd Segment Size        | float†    |
| 62 | Fwd Header Length.1         | int       |
| 63 | Fwd Avg Bytes/Bulk          | int       |
| 64 | Fwd Avg Packets/Bulk        | int       |
| 65 | Fwd Avg Bulk Rate           | int       |
| 66 | Bwd Avg Bytes/Bulk          | int       |
| 67 | Bwd Avg Packets/Bulk        | int       |
| 68 | Bwd Avg Bulk Rate           | int       |
| 69 | Subflow Fwd Packets         | int       |
| 70 | Subflow Fwd Bytes           | int       |
| 71 | Subflow Bwd Packets         | int       |
| 72 | Subflow Bwd Bytes           | int       |
| 73 | Init_Win_bytes_forward      | int       |
| 74 | Init_Win_bytes_backward     | int       |
| 75 | act_data_pkt_fwd            | int       |
| 76 | min_seg_size_forward        | int       |
| 77 | Active Mean                 | float†    |
| 78 | Active Std                  | float†    |
| 79 | Active Max                  | float†    |
| 80 | Active Min                  | float†    |
| 81 | Idle Mean                   | float†    |
| 82 | Idle Std                    | float†    |
| 83 | Idle Max                    | float†    |
| 84 | Idle Min                    | float†    |
| 85 | SimillarHTTP                | int, str* |
| 86 | Inbound                     | int       |
| 87 | Label                       | str*      |
