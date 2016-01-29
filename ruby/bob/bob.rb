class Bob
  def hey(remark)
    if is_silent?(remark)
      'Fine. Be that way!'
    elsif is_yelling?(remark)
      'Whoa, chill out!'
    elsif is_question?(remark)
      'Sure.'
    else
      'Whatever.'
    end
  end

  private

    def is_silent?(remark)
      remark.strip == ''
    end

    def is_yelling?(remark)
      remark.upcase == remark && remark.downcase != remark
    end

    def is_question?(remark)
      remark[-1] == '?'
    end
end
