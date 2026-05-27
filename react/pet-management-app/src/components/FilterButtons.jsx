function FilterButtons({setFilter}){
    return(
        <div style={{margin:'10px 0'}}>
            <button onClick={()=>setFilter('All')}>All</button>
            <button onClick={()=>setFilter('Active')}>Active</button>
            <button onClick={()=>setFilter('Completed')}>Completed</button>
        </div>
    )
}

export default FilterButtons