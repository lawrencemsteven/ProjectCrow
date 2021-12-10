import React, { useState, useEffect } from 'react'
import { useNavigate } from "react-router-dom";
import BackendRequest from '../../Managers/BackendRequest'
import { logout } from '../../auth/auth'

export default function Homes() {
	const navigate = useNavigate();
	const [homes, setHomes] = useState(null)
	let homes_to_show = []

	useEffect(() => {
		if (homes === null) {
			BackendRequest.get("api/homes/", (data)=>{
				setHomes(data.homes)
			});
		}
	}, [homes])

	if (homes !== null) {
		homes_to_show = homes
	}

	return (
		<div>
		<input type="button" onClick={() => {logout(); navigate("/login")}} value={"Logout"} />
			<div>
				{homes_to_show.map((home, index) => {
					return (
						<div key={index} className="row">
							<div className="col_0">{home.name}</div>
						</div>
					)
				})}
			</div>
		</div>
	)
}
