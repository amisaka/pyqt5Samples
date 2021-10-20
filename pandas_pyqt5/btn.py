def btn_clk(self):
    path = self.lineEdit.text()
    df = pd.read_csv(path)
    model = PandasModel(df)
    self.tableView.setModel(model)
