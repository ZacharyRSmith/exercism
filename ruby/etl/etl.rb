class ETL
  def self.transform(oldMap)
    oldMap.inject({ }) do |newMap, (score, ltrs)|
      ltrs.each { |ltr| newMap[ltr.downcase] = score }
      newMap
    end
  end
end