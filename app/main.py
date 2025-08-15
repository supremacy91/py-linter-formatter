def format_linter_error(error: dict) -> dict:
    return {**{
        ("line" if error_index == "line_number"
         else "column" if error_index == "column_number"
         else "message" if error_index == "text"
         else "name"): error_value
        for error_index, error_value in error.items()
        if error_index in ("line_number", "column_number", "text", "code")},
        **{"source": "flake8"}}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {**{"errors": [format_linter_error(error) for error in errors]
               for _ in range(1)},
            **{"path": file_path, "status": "failed" if errors else "passed"}}


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(report_file, report_error)
            for report_file, report_error in linter_report.items()]
