import unittest


class Train:
    Full = "Sorry the train is full currently wait for the next slot"
    Current_psg = "Currently the available Passenger are about : {}"
    Psg_Absent = "Passenger mising"
    Psg_Added = "New passenger {}"
    Psg_Eliminated = "Passenger Removed are about : {}"
    Train_Capacity = 0

    def __init__(self, Train_name: str, TrainCapacity: int):
        self.Train_name = Train_name
        self.TrainCapacity = TrainCapacity
        self.Psg = []

    def Add_psg(self, Psg_name: str) -> str:
        if len(self.Psg) == self.TrainCapacity:
            raise ValueError(self.Full)

        if Psg_name in self.Psg:
            raise ValueError(self.Current_psg.format(Psg_name))

        self.Psg.append(Psg_name)
        return self.Psg_Added.format(Psg_name)

    def Remove_psg(self, Psg_name: str) -> str:
        if Psg_name not in self.Psg:
            raise ValueError(self.Psg_Absent.format(Psg_name))

        self.Psg.remove(Psg_name)
        return self.Psg_Eliminated.format(Psg_name)



class NBM_Train(unittest.TestCase):
    def setUp(self):
        self.train = Train("Train", 2)

    def Test_Call(self):
        self.assertEqual(self.train.Train_name, "Nairobi_Mobasa_Express")
        self.assertEqual(self.train.TrainCapacity, 2)
        self.assertEqual(self.train.Psg, [])

    def Test_Add_Error(self):
        with self.assertRaises(ValueError) as ex:
            self.train.Add_psg("HEzron")
            self.train.Add_psg("Paul")
            self.train.Add_psg("Mark")
        expected_msg = str(ex.exception)
        actual_msg = "Train is full"
        self.assertEqual(expected_msg, actual_msg)

    def Add_psg_Error(self):
        with self.assertRaises(ValueError) as ex:
            self.train.Add_psg("Mathew")
            self.train.Add_psg("Andrew")
        expected_msg = str(ex.exception)
        actual_msg = "Passenger Andrew Exists"
        self.assertEqual(expected_msg, actual_msg)

    def Add_psg(self):
        self.train.Add_psg("Paul")
        self.assertEqual(len(self.train.Psg), 1)
        self.assertEqual(self.train.Add_psg("Mark"), "Mark Added")
        self.assertEqual(len(self.train.Psg), 2)

    def Removed_psg_Error(self):
        with self.assertRaises(ValueError) as ex:
            self.train.Remove_psg("Hezron")
        expected_msg = str(ex.exception)
        actual_msg = "Passenger Not Found"
        self.assertEqual(expected_msg, actual_msg)

    def Removed_psg(self):
        self.train.Add_psg("Hezron")
        self.assertEqual(len(self.train.Psg), 1)
        self.train.Remove_psg("Hezron")
        self.assertEqual(len(self.train.Psg), 0)
        self.train.Add_psg("Hezron")
        self.assertEqual(self.train.Remove_psg("Hezron"), "Removed Hezron")


if __name__ == "__main__":
    unittest.main()
