import * as React from 'react'
import Box from '@mui/material/Box'
import TextField from '@mui/material/TextField'
import { Select, FormControl, InputLabel, MenuItem, Button } from "@mui/material"
import { SelectChangeEvent } from '@mui/material/Select'
import { useState } from "react"
import CustomizedDialogs from "./Result"

export default function InputForm() {
	const [formValues, setFormValues] = useState({
		age: 18,
		sex: 'Male',
		cp: 'typical-angina',
		trestbps: 145.0,
		chol: 233.0,
		fbs: true,
		restecg: 'lv-hypertrophy',
		thalch: 150.0,
		exang: false,
		oldpeak: 2.3
	})

	const handleChange = (event: React.ChangeEvent<{ name?: string; value: unknown }> | SelectChangeEvent) => {
		const name = event.target.name as keyof typeof formValues
		setFormValues({
			...formValues,
			[name]: event.target.value,
		})
	}

	const [result, setResult] = useState(false)
	const [open, setOpen] = useState(false)

	const handleOpen = () => {
		setOpen(true)
	}

	const handleClose = () => {
		setOpen(false)
	}

	const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
		event.preventDefault()

		const response = await fetch('http://localhost:8000', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify(formValues),
		})

		const data = await response.json()

		setResult(Boolean(data.prediction[0]))
		handleOpen()
	}

	return (
		<FormControl component="fieldset">
			<Box
				component="form"
				onSubmit={handleSubmit}
				sx={{
					'& .MuiTextField-root': { m: 1, width: '25ch' },
					'& .MuiFormControl-root': { m: 1, width: '25ch' },
				}}
				noValidate
				autoComplete="off"
			>
				<div>
					<TextField
						required
						id="age"
						label="Age"
						variant="filled"
						value={formValues.age}
						type="number"
						inputProps={{ min: "0", step: "1", max: "100" }}
						onChange={handleChange}
						name="age"
					/>
					<FormControl variant="filled">
						<InputLabel id="sex">Sex</InputLabel>
						<Select
							labelId="sex"
							id="sex"
							value={formValues.sex}
							label="Sex"
							onChange={handleChange}
							name="sex"
						>
							<MenuItem value={"Male"}>Male</MenuItem>
							<MenuItem value={"Female"}>Female</MenuItem>
						</Select>
					</FormControl>
					<FormControl variant="filled">
						<InputLabel id="cp">cp</InputLabel>
						<Select
							labelId="cp"
							id="cp"
							value={formValues.cp}
							label="cp"
							onChange={handleChange}
							name="cp"
						>
							<MenuItem value={"asymptomatic"}>Asymptomatic</MenuItem>
							<MenuItem value={"non-anginal"}>Non-Anginal</MenuItem>
							<MenuItem value={"atypical-angina"}>Atypical Angina</MenuItem>
							<MenuItem value={"typical-angina"}>Typical Angina</MenuItem>
						</Select>
					</FormControl>
					<TextField
						id="trestbps"
						label="trestbps"
						value={formValues.trestbps}
						type="number"
						variant="filled"
						onChange={handleChange}
						name="trestbps"
					/>
					<TextField
						id="chol"
						label="chol"
						value={formValues.chol}
						type="number"
						variant="filled"
						onChange={handleChange}
						name="chol"
					/>
					<FormControl variant="filled">
						<InputLabel id="fbs">FBS</InputLabel>
						<Select
							labelId="fbs"
							id="fbs"
							value={formValues.fbs.toString()}
							label="fbs"
							onChange={handleChange}
							name="fbs"
						>
							<MenuItem value={"true"}>True</MenuItem>
							<MenuItem value={"false"}>False</MenuItem>
						</Select>
					</FormControl>
					<FormControl variant="filled">
						<InputLabel id="restecg">Rest ECG</InputLabel>
						<Select
							labelId="restecg"
							id="restecg"
							value={formValues.restecg}
							label="Rest ECG"
							onChange={handleChange}
							name="restecg"
						>
							<MenuItem value={"normal"}>Normal</MenuItem>
							<MenuItem value={"st-t-wave-abnormality"}>ST-T Wave Abnormality</MenuItem>
							<MenuItem value={"lv-hypertrophy"}>LV Hypertrophy</MenuItem>
						</Select>
					</FormControl>
					<TextField
						id="thalch"
						label="Thalch"
						value={formValues.thalch}
						type="number"
						variant="filled"
						onChange={handleChange}
						name="thalch"
					/>
					<FormControl variant="filled">
						<InputLabel id="exang">Exang</InputLabel>
						<Select
							labelId="exang"
							id="exang"
							value={formValues.exang.toString()}
							label="exang"
							onChange={handleChange}
							name="exang"
						>
							<MenuItem value={"true"}>True</MenuItem>
							<MenuItem value={"false"}>False</MenuItem>
						</Select>
					</FormControl>
					<TextField
						id="oldpeak"
						label="Old Peak"
						value={formValues.oldpeak}
						type="number"
						variant="filled"
						onChange={handleChange}
						name="oldpeak"
					/>
				</div>
				<Box
					display="flex"
					margin={1}
					marginTop={2}
				>
					<Button type="submit" variant="contained">Submit</Button>
				</Box>
			</Box>
			<CustomizedDialogs result={result} open={open} handleClose={handleClose} />
		</FormControl>
	)
}