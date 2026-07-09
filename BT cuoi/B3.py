#Câu 3 (Đồ thị & Thuật toán Dijkstra)
#Tại sao thuật toán Dijkstra lại cho kết quả sai khi đồ thị có chứa cạnh trọng số âm? 
#Hãy tự thiết kế một đồ thị có hướng nhỏ (gồm 3 đỉnh) làm phản ví dụ chứng minh sự sai lệch của bước "chốt đỉnh". 
#Đề xuất một thuật toán khác có thể thay thế Dijkstra trong trường hợp này


###vi thuat toan dijkstra la thuat toan tham lam, do do khi gap canh am thi thuat toan se sai vi no se chon canh am de di
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
}
### duong di ngan nhat tu A den D la A -> B -> C -> D = 1 + 2 + 1 = 4
### nhung neu gap canh am thi thuat toan se sai vi no se chon canh am de di

### ta co the dung thuat toan bellman-ford de tim duong di ngan nhat tu A den D, no lien tuc do xet va noi long cac canh cua do thi

