class LabReport:

    report_count = 0

    def __init__(
        self,
        patient_id,
        test_name,
        result,
        report_date
    ):

        LabReport.report_count += 1

        self.report_id = (
            f"L{LabReport.report_count:03}"
        )

        self.patient_id = patient_id

        self.test_name = test_name

        self.result = result

        self.report_date = report_date

    def display_details(self):

        print("\n==============================")

        print(
            "Report ID:",
            self.report_id
        )

        print(
            "Patient ID:",
            self.patient_id
        )

        print(
            "Test Name:",
            self.test_name
        )

        print(
            "Result:",
            self.result
        )

        print(
            "Report Date:",
            self.report_date
        )

        print("==============================")