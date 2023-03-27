import React, { useState, useEffect } from 'react'
import Web3 from 'web3'
import { ContractABI } from './ContractABI' // Replace with your contract ABI
import { ContractAddress } from './ContractAddress' // Replace with your contract address

const web3 = new Web3('https://mainnet.infura.io/v3/YOUR_PROJECT_ID') // Replace with your Infura project ID

const contract = new web3.eth.Contract(ContractABI, ContractAddress)

function Dashboard() {
  const [totalSupply, setTotalSupply] = useState(0)
  const [holderCount, setHolderCount] = useState(0)
  const [popularFunctions, setPopularFunctions] = useState([])

  useEffect(() => {
    async function fetchData() {
      // Get total supply
      const totalSupply = await contract.methods.totalSupply().call()
      setTotalSupply(totalSupply)

      // Get holder count
      const holderCount = await contract.methods.balanceOf(contract.options.address).call()
      setHolderCount(holderCount)

      // Get popular functions
      const popularFunctions = [
        { name: 'transfer', count: await getFunctionCallCount('transfer') },
        { name: 'approve', count: await getFunctionCallCount('approve') },
        { name: 'transferFrom', count: await getFunctionCallCount('transferFrom') },
      ]
      setPopularFunctions(popularFunctions)
    }

    fetchData()
  }, [])

  async function getFunctionCallCount(functionName) {
    const logs = await web3.eth.getPastLogs({
      fromBlock: 0,
      toBlock: 'latest',
      address: ContractAddress,
      topics: [web3.utils.sha3(functionName)]
    })
    return logs.length
  }

  return (
    <div>
      <div>Total Supply: {totalSupply}</div>
      <div>Holder Count: {holderCount}</div>
      <div>Popular Functions:</div>
      <ul>
        {popularFunctions.map((func) => (
          <li key={func.name}>{func.name}: {func.count}</li>
        ))}
      </ul>
    </div>
  )
}

export default Dashboard
