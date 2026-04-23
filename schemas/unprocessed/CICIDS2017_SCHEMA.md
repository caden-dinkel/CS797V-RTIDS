** `*` indicates string values present in the column 
   `†` indicates float values present in the column ** 
|    | Column                      | Types       |
|---:|:----------------------------|:------------|
|  0 | Flow ID                     | str*        |
|  1 | Source IP                   | str*        |
|  2 | Source Port                 | int         |
|  3 | Destination IP              | str*        |
|  4 | Destination Port            | int         |
|  5 | Protocol                    | int         |
|  6 | Timestamp                   | str*        |
|  7 | Flow Duration               | int         |
|  8 | Total Fwd Packets           | int         |
|  9 | Total Backward Packets      | int         |
| 10 | Total Length of Fwd Packets | float†, int |
| 11 | Total Length of Bwd Packets | float†, int |
| 12 | Fwd Packet Length Max       | float†, int |
| 13 | Fwd Packet Length Min       | float†, int |
| 14 | Fwd Packet Length Mean      | float†      |
| 15 | Fwd Packet Length Std       | float†      |
| 16 | Bwd Packet Length Max       | float†, int |
| 17 | Bwd Packet Length Min       | float†, int |
| 18 | Bwd Packet Length Mean      | float†      |
| 19 | Bwd Packet Length Std       | float†      |
| 20 | Flow Bytes/s                | float†      |
| 21 | Flow Packets/s              | float†      |
| 22 | Flow IAT Mean               | float†      |
| 23 | Flow IAT Std                | float†      |
| 24 | Flow IAT Max                | float†, int |
| 25 | Flow IAT Min                | float†, int |
| 26 | Fwd IAT Total               | float†, int |
| 27 | Fwd IAT Mean                | float†      |
| 28 | Fwd IAT Std                 | float†      |
| 29 | Fwd IAT Max                 | float†, int |
| 30 | Fwd IAT Min                 | float†, int |
| 31 | Bwd IAT Total               | float†, int |
| 32 | Bwd IAT Mean                | float†      |
| 33 | Bwd IAT Std                 | float†      |
| 34 | Bwd IAT Max                 | float†, int |
| 35 | Bwd IAT Min                 | float†, int |
| 36 | Fwd PSH Flags               | int         |
| 37 | Bwd PSH Flags               | int         |
| 38 | Fwd URG Flags               | int         |
| 39 | Bwd URG Flags               | int         |
| 40 | Fwd Header Length           | int         |
| 41 | Bwd Header Length           | int         |
| 42 | Fwd Packets/s               | float†      |
| 43 | Bwd Packets/s               | float†      |
| 44 | Min Packet Length           | float†, int |
| 45 | Max Packet Length           | float†, int |
| 46 | Packet Length Mean          | float†      |
| 47 | Packet Length Std           | float†      |
| 48 | Packet Length Variance      | float†      |
| 49 | FIN Flag Count              | int         |
| 50 | SYN Flag Count              | int         |
| 51 | RST Flag Count              | int         |
| 52 | PSH Flag Count              | int         |
| 53 | ACK Flag Count              | int         |
| 54 | URG Flag Count              | int         |
| 55 | CWE Flag Count              | int         |
| 56 | ECE Flag Count              | int         |
| 57 | Down/Up Ratio               | float†, int |
| 58 | Average Packet Size         | float†      |
| 59 | Avg Fwd Segment Size        | float†      |
| 60 | Avg Bwd Segment Size        | float†      |
| 61 | Fwd Header Length.1         | int         |
| 62 | Fwd Avg Bytes/Bulk          | int         |
| 63 | Fwd Avg Packets/Bulk        | int         |
| 64 | Fwd Avg Bulk Rate           | int         |
| 65 | Bwd Avg Bytes/Bulk          | int         |
| 66 | Bwd Avg Packets/Bulk        | int         |
| 67 | Bwd Avg Bulk Rate           | int         |
| 68 | Subflow Fwd Packets         | int         |
| 69 | Subflow Fwd Bytes           | int         |
| 70 | Subflow Bwd Packets         | int         |
| 71 | Subflow Bwd Bytes           | int         |
| 72 | Init_Win_bytes_forward      | int         |
| 73 | Init_Win_bytes_backward     | int         |
| 74 | act_data_pkt_fwd            | int         |
| 75 | min_seg_size_forward        | int         |
| 76 | Active Mean                 | float†      |
| 77 | Active Std                  | float†      |
| 78 | Active Max                  | float†, int |
| 79 | Active Min                  | float†, int |
| 80 | Idle Mean                   | float†      |
| 81 | Idle Std                    | float†      |
| 82 | Idle Max                    | float†, int |
| 83 | Idle Min                    | float†, int |
| 84 | Label                       | str*        |
